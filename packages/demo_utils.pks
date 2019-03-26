create or replace package demo_utils authid current_user is 

    function login(p_username in varchar2,
                   p_password in varchar2)
                   return boolean;

end demo_utils;