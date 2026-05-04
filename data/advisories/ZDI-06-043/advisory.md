# ZDI-06-043: Novell Netware Client Print Provider Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-043
- **ZDI-CAN:** ZDI-CAN-100
- **Date:** 2006-11-29
- **CVE:** CVE-2006-5854
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** Netware
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-043/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of the Novell Netware Client. Authentication is not required to exploit this vulnerability. The specific flaw exists in a print provider installed by the Netware Client. The nwspool.dll library does not properly handle long arguments to the Win32 EnumPrinters() and OpenPrinter() functions. Exceeding 458 bytes in the first argument to OpenPrinter() or 524 bytes in the second argument to EnumPrinters() results in an exploitable buffer overflow within the Spooler service. This vulnerability can be exploited remotely via Remote Procedure Call (RPC) requests to the Spooler service. The Spooler exposes the "spoolss" named pipe, which allows an anonymous user to issue certain spooler commands. These include the OpenPrinter() and EnumPrinters() calls required to exploit this vulnerability.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/search.do?cmd=displayKC&externalId=3125538&sliceId=SAL_Public

## Disclosure Timeline

- 2006-10-02 - Vulnerability reported to vendor
- 2006-11-29 - Coordinated public release of advisory
