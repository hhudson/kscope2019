create or replace package ut_demo as
  --%suite(Kscope demo utplsql procedures)
  
  --%test(Demonstrate random intentional failure)
  procedure demo;

  --%test(Test the login function)
  procedure test_login;

end ut_demo;
/