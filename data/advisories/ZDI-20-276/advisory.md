# ZDI-20-276: Horde Groupware Webmail Edition edit Page Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-276
- **ZDI-CAN:** ZDI-CAN-10469
- **Date:** 2020-03-10
- **CVE:** CVE-2020-8865
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Horde
- **Affected Products:** Groupware Webmail Edition
- **Credit:** Andrea Cardaci
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-276/
## Vulnerability Details

This vulnerability allows remote attackers to execute local PHP files on affected installations of Horde Groupware Webmail Edition. Authentication is required to exploit this vulnerability. The specific flaw exists within edit.php. When parsing the params[template] parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the www-data user.

## Additional Details

Horde has issued an update to correct this vulnerability. More details can be found at: https://lists.horde.org/archives/announce/2020/001286.html

## Disclosure Timeline

- 2020-02-28 - Vulnerability reported to vendor
- 2020-03-10 - Coordinated public release of advisory
