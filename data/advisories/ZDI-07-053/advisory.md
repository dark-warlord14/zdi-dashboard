# ZDI-07-053: Microsoft ISA Server SOCKS4 Proxy Connection Leakage Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-053
- **ZDI-CAN:** ZDI-CAN-018
- **Date:** 2007-09-20
- **CVE:** CVE-2007-4991
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** ISA Server
- **Credit:** CIRT.DK
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-053/
## Vulnerability Details

This vulnerability allows remote attackers to extract IP addresses visited through the SOCKS4 Proxy on vulnerable ISA Server installations. Authentication is not required to exploit this vulnerability. This specific flaw exists when an empty packet is sent to the SOCKS4. The server will return a packet containing the last IP address it proxied to.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/downloads/details.aspx?FamilyID=A05A074A-5033-4792-AF8B-58B90D841436&displaylang=en

## Disclosure Timeline

- 2006-01-30 - Vulnerability reported to vendor
- 2007-09-20 - Coordinated public release of advisory
