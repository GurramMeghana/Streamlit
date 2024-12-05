import streamlit as st
from snowflake.snowpark import session

st.title("Snowflake User Creation")

st.header("Snowflake Account Details")
snowflake_account = st.text_input("Enter Snowflake Account URL:")
snowflake_user = st.text_input("Enter Snowflake User:")
snowflake_password = st.text_input("Enter Snowflake Password:", type="password")

st.header("New Snowflake User Details")
user_name = st.text_input("Enter User name:")
user_password = st.text_input("Enter User Password:", type="password")
default_role = st.text_input("Enter Default Role:")
default_warehouse = st.text_input("Enter Default Warehouse:")

if st.button("Create User"):
    if not all ([snowflake_account,snowflake_user,snowflake_password,user_name,user_password,default_role,default_warehouse]):
        st.error("All fields required")
    else:
        try:
            session_params ={
                "account":snowflake_account,
                "user": snowflake_user,
                "Password":snowflake_password,
                "ROLE": "ACCOUNTADMIN"
            }
            session=session.builder.configs(session_params).create()
            
            session.sql("USE ROLE ACCOUNTADMIN;").collect()
            create_user_query = f"""
            CREATE USER IF NOT EXISTS "{user_name}"
            EMAIL = '{user_name}'
            PASSWORD = '{user_password}'
            COMMENT = 'User created for {user_name}.'
            MUST_CHANGE_PASSWORD = TRUE
            LOGIN_NAME = '{user_name.upper()}'
            DISPLAY_NAME = '{user_name.title()}'
            FIRST_NAME = '{user_name.split(".")[0].title()}'
            LAST_NAME = '{user_name.split(".")[1].title()}'
            DEFAULT_ROLE = '{default_role}'
            DEFAULT_WAREHOUSE = '{default_warehouse}';
            """
            session.sql(create_user_query).collect()
            st.success(f"User created successfully")
        except:
            st.error("user not created")
            
