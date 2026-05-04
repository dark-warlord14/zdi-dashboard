# ZDI-15-367: BitTorrent Bootstrap Improper Indexing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-367
- **ZDI-CAN:** ZDI-CAN-2794
- **Date:** 2015-07-29
- **CVE:** CVE-2015-5685
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** BitTorrent
- **Affected Products:** Bootstrap
- **Credit:** Team_LPJ@BoB
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-367/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of BitTorrent Bootstrap. User interaction is not required to exploit this vulnerability. The specific flaw exists within the handling of arguments passed to the lazy_bdecode function. By sending a specific crafted packet an attacker can access data outside the bounds of an allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

BitTorrent has issued an update to correct this vulnerability. More details can be found at: https://github.com/bittorrent/bootstrap-dht/commit/e809ea80e3527e32c40756eddd8b2ae44bc3af1a

## Disclosure Timeline

- 2015-04-13 - Vulnerability reported to vendor
- 2015-07-29 - Coordinated public release of advisory
