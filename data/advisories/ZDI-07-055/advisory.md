# ZDI-07-055: Microsoft Windows DCERPC Authentication Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-055
- **ZDI-CAN:** ZDI-CAN-164
- **Date:** 2007-10-10
- **CVE:** CVE-2007-2228
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows 2000 SP4 Windows XP SP2 Windows 2003 SP1 Windows Vista
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-055/
## Vulnerability Details

This vulnerability allows remote attackers to crash systems with vulnerable installations of the Microsoft Windows operating system. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RPC runtime library rpcrt4.dll during the parsing of RPC-level authentication messages. When parsing packets with the authentication type of NTLMSSP and the authentication level of PACKET, an invalid memory dereference can occur if the verification trailer signature is initialized to 0 as opposed to the standard NTLM signature. Successful exploitation crashes the RPC service and subsequently the entire operating system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms07-058.mspx

## Disclosure Timeline

- 2007-02-05 - Vulnerability reported to vendor
- 2007-10-10 - Coordinated public release of advisory
