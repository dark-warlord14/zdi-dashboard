# ZDI-16-341: Apple Safari DataCue Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-341
- **ZDI-CAN:** ZDI-CAN-3576
- **Date:** 2016-05-19
- **CVE:** CVE-2016-1854
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-341/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of DataCue objects. By manipulating a document's elements an attacker can cause a DataCue object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206568

## Disclosure Timeline

- 2016-03-11 - Vulnerability reported to vendor
- 2016-05-19 - Coordinated public release of advisory
