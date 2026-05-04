# ZDI-19-633: Foxit PhantomPDF Button Calculate Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-633
- **ZDI-CAN:** ZDI-CAN-8757
- **Date:** 2019-07-05
- **CVE:** CVE-2019-13316
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** RockStar
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-633/
## Vulnerability Details

This vulnerability allows remote atackers to execute arbitrary code on affected installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Calculate actions. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-06-07 - Vulnerability reported to vendor
- 2019-07-05 - Coordinated public release of advisory
