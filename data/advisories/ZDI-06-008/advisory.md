# ZDI-06-008: Novell GroupWise Messenger Accept-Language Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-008
- **ZDI-CAN:** ZDI-CAN-028
- **Date:** 2006-04-13
- **CVE:** CVE-2006-0992
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** GroupWise Messenger
- **Credit:** CIRT.DK
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-008/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of the Novell GroupWise Messenger. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Novell Messaging Agent, a web server that listens by default on TCP port 8300. Insufficient length checks during the parsing of long parameters within the Accept-Language header results in an exploitable stack overflow under the context of the SYSTEM user.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://support.novell.com/cgi-bin/search/searchtid.cgi?10100861.htm

## Disclosure Timeline

- 2006-03-16 - Vulnerability reported to vendor
- 2006-04-13 - Coordinated public release of advisory
