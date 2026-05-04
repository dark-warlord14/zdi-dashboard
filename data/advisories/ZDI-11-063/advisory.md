# ZDI-11-063: Microsoft Visio 2007 LZW Stream Decompression Exception Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-063
- **ZDI-CAN:** ZDI-CAN-813
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0092
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Other
- **Credit:** Procyun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-063/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Visio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Visio handles parsing the VisioDocument stream. Upon handling a malformed stream, the application will raise an exception. While handling this exception, the application will access the vtable of an object that hasn't been completely initialized yet. Successful exploitation could lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms11-008.mspx

## Disclosure Timeline

- 2010-06-01 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory
