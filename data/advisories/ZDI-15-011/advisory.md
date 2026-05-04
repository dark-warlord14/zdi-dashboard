# ZDI-15-011: Apple Mac OS X DFont Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-011
- **ZDI-CAN:** ZDI-CAN-2532
- **Date:** 2015-01-27
- **CVE:** CVE-2014-4484
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Gaurav Baruah
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-011/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Mac OSX. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of a dfont file. When processing a malformed dfont file, a specified value is parsed from the file and passed to the memmove API call which can cause memory corruption. A remote attacker can use this to execute remote code under the context of the user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/en-us/HT204244

## Disclosure Timeline

- 2014-10-22 - Vulnerability reported to vendor
- 2015-01-27 - Coordinated public release of advisory
