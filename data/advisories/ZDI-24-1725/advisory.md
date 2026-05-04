# ZDI-24-1725: Webmin CGI Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1725
- **ZDI-CAN:** ZDI-CAN-22346
- **Date:** 2024-12-20
- **CVE:** CVE-2024-12828
- **CVSS:** 9.9
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Webmin
- **Affected Products:** Webmin
- **Credit:** ptrstr
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1725/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Webmin. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of CGI requests. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Webmin has issued an update to correct this vulnerability. More details can be found at: https://github.com/webmin/authentic-theme/commit/61e5b10227b50407e3c6ac494ffbd4385d1b59df

## Disclosure Timeline

- 2024-03-28 - Vulnerability reported to vendor
- 2024-12-20 - Coordinated public release of advisory
- 2024-12-20 - Advisory Updated
