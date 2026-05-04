# ZDI-21-281: Adobe Creative Cloud Improper Privilege Management Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-281
- **ZDI-CAN:** ZDI-CAN-12450
- **Date:** 2021-03-15
- **CVE:** CVE-2021-21069
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Creative Cloud
- **Credit:** rookuu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-281/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Adobe Creative Cloud on Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Adobe privileged helper tool. The issue lies in the lack of proper validation of the helper clients. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/creative-cloud/apsb21-18.html

## Disclosure Timeline

- 2021-02-03 - Vulnerability reported to vendor
- 2021-03-15 - Coordinated public release of advisory
