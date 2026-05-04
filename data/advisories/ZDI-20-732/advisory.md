# ZDI-20-732: (Pwn2Own) Rockwell Automation Studio 5000 Version Missing Authentication for Critical Function Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-732
- **ZDI-CAN:** ZDI-CAN-10291
- **Date:** 2020-06-22
- **CVE:** CVE-2020-12027
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** Studio 5000
- **Credit:** Chris Anastasio (muffin) and Steven Seeley (mr_me) of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-732/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Rockwell Automation Studio 5000. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the Version parameter provided to hmi_isapi.dll. The issue results from a lack of authentication required to query the server. An attacker can leverage this in conjunction with other vulnerability to execute code in the context of the current process.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://rockwellautomation.custhelp.com/app/answers/detail/a_id/1126944

## Disclosure Timeline

- 2020-01-30 - Vulnerability reported to vendor
- 2020-06-22 - Coordinated public release of advisory
