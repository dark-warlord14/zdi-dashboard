# ZDI-15-370: (Pwn2Own) Adobe Reader Portfolio Preview Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-370
- **ZDI-CAN:** ZDI-CAN-3104
- **Date:** 2015-07-29
- **CVE:** CVE-2015-5106
- **CVSS:** 6.6
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Nicolas Joly
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-370/
## Vulnerability Details

This vulnerability allows attackers to elevate privileges on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw occurs within the handling of Portfolio documents. When previewing Portfolio documents, the broker process utilizes higher privileges than necessary. An attacker can leverage this vulnerability to bypass intended access restrictions and perform a transition from Low Integrity to Medium Integrity.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-15.html

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-07-29 - Coordinated public release of advisory
