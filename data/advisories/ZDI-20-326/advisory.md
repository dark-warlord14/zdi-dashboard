# ZDI-20-326: Adobe Acrobat Pro DC Genuine Software Service Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-326
- **ZDI-CAN:** ZDI-CAN-9597
- **Date:** 2020-03-19
- **CVE:** CVE-2020-3766
- **CVSS:** 8.4
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Glenn Lloyd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-326/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Adobe Acrobat Pro DC. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Adobe Genuine Software Service. The issue results from incorrect permissions set on a resource used by the service. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/integrity_service/apsb20-12.html

## Disclosure Timeline

- 2019-12-04 - Vulnerability reported to vendor
- 2020-03-19 - Coordinated public release of advisory
