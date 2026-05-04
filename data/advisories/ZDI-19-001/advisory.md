# ZDI-19-001: Adobe Acrobat Pro DC Preflight setDefaultLibrary Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-001
- **ZDI-CAN:** ZDI-CAN-6656
- **Date:** 2019-01-04
- **CVE:** CVE-2018-16011
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Sebastian Apelt (@bitshifter123)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-001/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Preflight setDefaultLibrary method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-02.html

## Disclosure Timeline

- 2018-08-30 - Vulnerability reported to vendor
- 2019-01-04 - Coordinated public release of advisory
- 2020-08-18 - Advisory Updated
