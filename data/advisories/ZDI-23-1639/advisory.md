# ZDI-23-1639: Microsoft .NET FormatFtpCommand CRLF Injection Arbitrary File Write and Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1639
- **ZDI-CAN:** ZDI-CAN-21960
- **Date:** 2023-11-15
- **CVE:** CVE-2023-36049
- **CVSS:** 7.6
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:H/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** .NET
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1639/
## Vulnerability Details

This vulnerability allows remote attackers to create or delete arbitrary files on FTP servers implemented using affected versions of Microsoft .NET. Interaction with the .NET framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the FormatFtpCommand method. The issue results from the incorrect neutralization of CRLF sequences. An attacker can leverage this vulnerability to write or delete files in the context of the FTP server.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36049

## Disclosure Timeline

- 2023-08-16 - Vulnerability reported to vendor
- 2023-11-15 - Coordinated public release of advisory
