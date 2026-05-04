# ZDI-06-016: Novell eDirectory 8.8 NDS Server Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-016
- **ZDI-CAN:** ZDI-CAN-027
- **Date:** 2006-06-13
- **CVE:** CVE-2006-2496
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** CIRT.DK
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-016/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell eDirectory. Exploitation does not require authentication. The specific flaw exists within the iMonitor NDS Server, which by default exposes an HTTP interface on TCP port 8028 and an HTTPS interface on TCP port 8030. During the parsing of long URIs to the 'nds' path a trivially exploitable stack-based buffer overflow occurs.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://support.novell.com/cgi-bin/search/searchtid.cgi?/2973759.htm

## Disclosure Timeline

- 2006-03-20 - Vulnerability reported to vendor
- 2006-06-13 - Coordinated public release of advisory
