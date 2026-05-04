# ZDI-20-304: Foxit Studio Photo TIF File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-304
- **ZDI-CAN:** ZDI-CAN-9774
- **Date:** 2020-03-16
- **CVE:** CVE-2020-8881
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Studio Photo
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-304/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit Studio Photo. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of TIF files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-11-14 - Vulnerability reported to vendor
- 2020-03-16 - Coordinated public release of advisory
