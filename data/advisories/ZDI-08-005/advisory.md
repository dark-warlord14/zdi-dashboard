# ZDI-08-005: Novell Client NWSPOOL.DLL EnumPrinters Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-005
- **ZDI-CAN:** ZDI-CAN-266
- **Date:** 2008-02-11
- **CVE:** CVE-2008-0639
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** Netware
- **Credit:** Anonymous and Avosani Gabriele
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-005/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of the Novell Netware Client. Authentication is not required to exploit this vulnerability. The specific flaw exists in nwspool.dll which is responsible for handling RPC requests through the spoolss named pipe. The EnumPrinters function exposed by this DLL contains a logical flaw allowing an attacker to bypass a patch introduced to prevent the vulnerability described in ZDI-07-045. Exploitation of this vulnerability leads to arbitrary code execution in the context of the SYSTEM user.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=SszG22IIugM~

## Disclosure Timeline

- 2007-12-11 - Vulnerability reported to vendor
- 2008-02-11 - Coordinated public release of advisory
