# ZDI-16-198: Mozilla Firefox nsHtml5TreeBuilder Array Indexing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-198
- **ZDI-CAN:** ZDI-CAN-3545
- **Date:** 2016-03-11
- **CVE:** CVE-2016-1960
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** ca0nguyen
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-198/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of HTML5 end tags. The issue lies in the failure to check for an index becoming negative, allowing for out-of-bounds indexing. An attacker can leverage this vulnerability to execute code within the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2016-23/

## Disclosure Timeline

- 2016-02-04 - Vulnerability reported to vendor
- 2016-03-11 - Coordinated public release of advisory
