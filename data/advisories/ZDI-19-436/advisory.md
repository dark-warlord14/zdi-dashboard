# ZDI-19-436: Foxit PhantomPDF blink_core HTML Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-436
- **ZDI-CAN:** ZDI-CAN-7844
- **Date:** 2019-04-29
- **CVE:** CVE-2019-6762
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-436/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the conversion of HTML files to PDF. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-03-01 - Vulnerability reported to vendor
- 2019-04-29 - Coordinated public release of advisory
