# ZDI-07-076: Microsoft Windows Message Queuing Service Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-076
- **ZDI-CAN:** ZDI-CAN-178
- **Date:** 2007-12-11
- **CVE:** CVE-2007-3039
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Windows 2000 SP4 Windows XP SP2
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-076/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows with the Message Queuing Service enabled. Authentication is not required to exploit this vulnerability. The specific flaw exists in the RPC interface defined on port 2103 with UUID fdb3a030-065f-11d1-bb9b-00a024ea5525. During the processing of opnum 0x06 the service copies user-supplied information into a fixed length stack buffer. Sending at least 300 bytes will trigger a stack based buffer overflow due to a vulnerable wcscat() call. Exploitation of this issue can result in arbitrary code execution.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms07-065.mspx

## Disclosure Timeline

- 2007-04-02 - Vulnerability reported to vendor
- 2007-12-11 - Coordinated public release of advisory
