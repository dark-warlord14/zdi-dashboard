# ZDI-13-005: Microsoft .NET Framework EncoderParameters.ConvertToMemory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-005
- **ZDI-CAN:** ZDI-CAN-1515
- **Date:** 2013-02-01
- **CVE:** CVE-2013-0002
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** .NET
- **Credit:** Vitaliy Toropov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-005/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft .NET Framework. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the System.Drawing.Imaging.EncoderParameters.ConvertToMemory() method inside the .NET Framework. The function allocates an array based on the value of the parameter this.param.Length and then uses a loop terminated by the same parameter to fill the array with data. If another thread changes the value of this.param.Length between the array creation and loop this can result in a heap buffer overflow that can lead to remote code execution under the context of the current program.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/MS13-004

## Disclosure Timeline

- 2012-07-16 - Vulnerability reported to vendor
- 2013-02-01 - Coordinated public release of advisory
