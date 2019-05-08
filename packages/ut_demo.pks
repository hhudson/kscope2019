
create or replace package test_hhh as
  --%suite(Between string function)
  
  --%test(Random intentional failure)
  procedure blerg;

  --%test(tests the login function)
  procedure test_login;

end test_hhh;
/