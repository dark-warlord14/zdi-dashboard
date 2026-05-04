# ZDI-25-414: Ruby WEBrick read_header HTTP Request Smuggling Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-414
- **ZDI-CAN:** ZDI-CAN-21876
- **Date:** 2025-06-23
- **CVE:** CVE-2025-6442
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:H/A:N
- **Affected Vendors:** Ruby
- **Affected Products:** WEBrick
- **Credit:** yadhukrishnam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-414/
## Vulnerability Details

This vulnerability allows remote attackers to smuggle arbitrary HTTP requests on affected installations of Ruby WEBrick. This issue is exploitable when the product is deployed behind an HTTP proxy that fulfills specific conditions. The specific flaw exists within the read_headers method. The issue results from the inconsistent parsing of terminators of HTTP headers. An attacker can leverage this vulnerability to smuggle arbitrary HTTP requests.

## Additional Details

Ruby has issued an update to correct this vulnerability. More details can be found at: https://github.com/ruby/webrick/commit/ee60354bcb84ec33b9245e1d1aa6e1f7e8132101#diff-ad02984d873efb089aa51551bc6b7d307a53e0ba1ac439e91d69c2e58a478864

## Disclosure Timeline

- 2023-09-13 - Vulnerability reported to vendor
- 2025-06-23 - Coordinated public release of advisory
- 2025-06-23 - Advisory Updated
