# ZDI-23-1169: Avira Free Antivirus Integer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1169
- **ZDI-CAN:** ZDI-CAN-19836
- **Date:** 2023-08-24
- **CVE:** CVE-2023-1900
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Avira
- **Affected Products:** Free Antivirus
- **Credit:** rac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1169/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Avira Free Antivirus. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the netprotection network filter driver. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Avira has issued an update to correct this vulnerability. More details can be found at: https://support.norton.com/sp/static/external/tools/security-advisories.html

## Disclosure Timeline

- 2023-03-22 - Vulnerability reported to vendor
- 2023-08-24 - Coordinated public release of advisory
