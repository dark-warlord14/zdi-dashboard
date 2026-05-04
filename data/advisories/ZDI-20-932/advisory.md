# ZDI-20-932: Foxit PhantomPDF SetLocalDescription Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-932
- **ZDI-CAN:** ZDI-CAN-10972
- **Date:** 2020-08-04
- **CVE:** CVE-2020-15637
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-932/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the SetLocalDescription method. By performing actions in JavaScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.html

## Disclosure Timeline

- 2020-04-23 - Vulnerability reported to vendor
- 2020-08-04 - Coordinated public release of advisory
