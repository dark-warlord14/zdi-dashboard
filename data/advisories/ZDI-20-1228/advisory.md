# ZDI-20-1228: Foxit PhantomPDF GIF File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1228
- **ZDI-CAN:** ZDI-CAN-11135
- **Date:** 2020-09-29
- **CVE:** CVE-2020-17410
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** Dominik Chyliński
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1228/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of GIF files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2020-06-02 - Vulnerability reported to vendor
- 2020-09-29 - Coordinated public release of advisory
- 2020-10-09 - Advisory Updated
