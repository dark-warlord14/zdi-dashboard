# ZDI-16-199: Mozilla Firefox nsHTMLDocument SetBody Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-199
- **ZDI-CAN:** ZDI-CAN-3574
- **Date:** 2016-03-11
- **CVE:** CVE-2016-1961
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** lokihardt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-199/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of nsHTMLDocument objects. By manipulating a document's elements an attacker can force a nsHTMLDocument object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2016-24/

## Disclosure Timeline

- 2016-02-18 - Vulnerability reported to vendor
- 2016-03-11 - Coordinated public release of advisory
