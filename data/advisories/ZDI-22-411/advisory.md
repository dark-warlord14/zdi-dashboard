# ZDI-22-411: (Pwn2Own) Cisco RV340 upload.cgi JSON Command Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-411
- **ZDI-CAN:** ZDI-CAN-15883
- **Date:** 2022-02-22
- **CVE:** CVE-2022-20707
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Bien Pham (@bienpnn) from Team Orca of Sea Security (security.sea.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-411/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to escalate privileges on affected installations of Cisco RV340 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of POST request parameters provided to the upload.cgi endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the www-data user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-mult-vuln-KA9PK6D

## Disclosure Timeline

- 2021-12-03 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory
