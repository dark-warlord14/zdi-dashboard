# ZDI-07-045: Novell Client NWSPOOL.DLL Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-045
- **ZDI-CAN:** ZDI-CAN-146
- **Date:** 2007-08-06
- **CVE:** CVE-2007-2954
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** eDirectory
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-045/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of the Novell Netware Client. Authentication is not required to exploit this vulnerability. The specific flaw exists in nwspool.dll which is responsible for handling RPC requests through the spoolss named pipe. Several RPC functions exposed by this DLL do not properly verify argument sizes and subsequently copy user-supplied data to a stack-based buffer resulting in an exploitable overflow.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://support.novell.com/docs/Readmes/InfoDocument/patchbuilder/readme_5005400.html

## Disclosure Timeline

- 2007-02-16 - Vulnerability reported to vendor
- 2007-08-06 - Coordinated public release of advisory
