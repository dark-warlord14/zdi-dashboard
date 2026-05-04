# ZDI-07-022: CA BrightStor ArcServe Media Server Multiple Buffer Overflow Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-07-022
- **ZDI-CAN:** ZDI-CAN-171
- **Date:** 2007-04-24
- **CVE:** CVE-2007-2139
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** BrightStor ARCserve Server
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-022/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Computer Associates BrightStor ARCserve Media Server. User interaction is not required to exploit this vulnerability. The specific flaw exists in the SUN RPC service which binds to a randomly chosen high TCP port. The target port can be obtained by querying the port mapper. Multiple stack-based buffer overflows exist during the parsing of malformed RPC strings. Exploitation of these overflows can result in arbitrary code execution.

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: http://supportconnectw.ca.com/public/storage/infodocs/babmedser-secnotice.asp

## Disclosure Timeline

- 2007-03-08 - Vulnerability reported to vendor
- 2007-04-24 - Coordinated public release of advisory
