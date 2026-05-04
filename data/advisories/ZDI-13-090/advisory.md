# ZDI-13-090: (Pwn2Own) Mozilla Firefox nsHTMLEditRules Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-090
- **ZDI-CAN:** ZDI-CAN-1825
- **Date:** 2013-05-29
- **CVE:** CVE-2013-0787
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** VUPEN Security [ http://www.vupen.com ]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-090/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of nsHTMLEditRules objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.mozilla.org/show_bug.cgi?id=848644

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
