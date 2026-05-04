# ZDI-20-211: Foxit PhantomPDF fxhtml2pdf Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-211
- **ZDI-CAN:** ZDI-CAN-9560
- **Date:** 2020-02-11
- **CVE:** CVE-2020-8855
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-211/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the fxhtml2pdf.exe module. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-11-12 - Vulnerability reported to vendor
- 2020-02-11 - Coordinated public release of advisory
