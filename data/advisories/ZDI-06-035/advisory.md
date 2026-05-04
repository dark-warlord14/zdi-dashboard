# ZDI-06-035: Novell eDirectory NDS Server Host Header Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-035
- **ZDI-CAN:** ZDI-CAN-081
- **Date:** 2006-10-26
- **CVE:** CVE-2006-5478
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** Manuel Santamarina Suarez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-035/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell eDirectory. Authentication is not required to exploit this vulnerability. The specific flaw exists within the httpstk.dll library within the dhost.exe web interface of the eDirectory Host Environment. The web interface does not validate the length of the HTTP Host header prior to using the value of that header in an HTTP redirect. This results in an exploitable stack-based buffer overflow.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&docType=kc&externalId=3723994&sliceId=SAL_Public&dialogID=16776123&stateId=1%200%202648401

## Disclosure Timeline

- 2006-08-14 - Vulnerability reported to vendor
- 2006-10-26 - Coordinated public release of advisory
