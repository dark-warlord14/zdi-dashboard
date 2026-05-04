# ZDI-21-1333: Adobe Creative Cloud Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1333
- **ZDI-CAN:** ZDI-CAN-14772
- **Date:** 2021-11-24
- **CVE:** CVE-2021-43019
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Creative Cloud
- **Credit:** Jokubas Arsoba
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1333/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Adobe Creative Cloud. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permsissions set on a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/creative-cloud/apsb21-111.html

## Disclosure Timeline

- 2021-09-01 - Vulnerability reported to vendor
- 2021-11-24 - Coordinated public release of advisory
