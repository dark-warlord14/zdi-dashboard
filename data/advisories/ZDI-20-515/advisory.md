# ZDI-20-515: Foxit PhantomPDF Export Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-515
- **ZDI-CAN:** ZDI-CAN-9865
- **Date:** 2020-04-16
- **CVE:** CVE-2020-10908
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-515/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Export command of the communication API. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-12-19 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
