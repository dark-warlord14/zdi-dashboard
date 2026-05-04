# ZDI-18-1413: Adobe Reader DC Onix GetRecordRM Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1413
- **ZDI-CAN:** ZDI-CAN-7038
- **Date:** 2018-12-17
- **CVE:** CVE-2018-16007
- **CVSS:** 8.6
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Sebastian Apelt (@bitshifter123)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1413/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the GetRecordRM method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-41.html

## Disclosure Timeline

- 2018-08-01 - Vulnerability reported to vendor
- 2018-12-17 - Coordinated public release of advisory
