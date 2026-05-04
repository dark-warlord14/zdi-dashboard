# ZDI-14-214: Foxit PDF SDK DLL FPDFBookmark_GetTitle Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-214
- **ZDI-CAN:** ZDI-CAN-1983
- **Date:** 2014-06-30
- **CVE:** CVE-2014-4646
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Foxit PDF SDK DLL
- **Credit:** John Leitch
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-214/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on software built with vulnerable versions of the Foxit SDK. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the FPDFBookmark_GetTitle() function. An error in evaluating the safety of the copy allows for an attacker to overflow the provided buffer in some circumstances. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: http://www.foxitsoftware.com/support/security_bulletins.php#FRD-20

## Disclosure Timeline

- 2014-04-22 - Vulnerability reported to vendor
- 2014-06-30 - Coordinated public release of advisory
