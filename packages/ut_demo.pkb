
create or replace package body test_hhh
is 


procedure blerg
is
begin
    ut.expect('hayden').to_equal('haydenhh');
end blerg;

procedure test_login
is 
l_success boolean;
begin
  l_success := demo_utils.login(p_username => 'Hayden',
                                p_password => 'Oradoc_db1');
  ut.expect( l_success ).to_be_true();
end test_login;

end test_hhh;
/