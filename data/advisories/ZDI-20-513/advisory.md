# ZDI-20-513: Foxit PhantomPDF CombineFiles Arbitrary File Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-513
- **ZDI-CAN:** ZDI-CAN-9830
- **Date:** 2020-04-16
- **CVE:** CVE-2020-10892
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-513/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the communication API. The issue lies in the handling of the CombineFiles command, which allows an arbitrary file write with attacker controlled data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-12-19 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
