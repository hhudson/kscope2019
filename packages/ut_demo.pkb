create or replace package body ut_demo
is 



procedure demo
is
begin
    ut.expect('Seattle').to_equal('Seattle');
end demo;






procedure test_login
is 
l_success boolean;
begin

  l_success := demo_utils.login(p_username => 'Hayden',
                                p_password => 'Oradoc_db1');
  ut.expect( l_success ).to_be_true();

end test_login;






end ut_demo;
/