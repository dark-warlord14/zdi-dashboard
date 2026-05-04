# ZDI-21-614: Foxit PhantomPDF XFA Template Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-614
- **ZDI-CAN:** ZDI-CAN-13531
- **Date:** 2021-05-26
- **CVE:** CVE-2021-31476
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** cece
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-614/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of XFA templates. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2021-04-22 - Vulnerability reported to vendor
- 2021-05-26 - Coordinated public release of advisory
