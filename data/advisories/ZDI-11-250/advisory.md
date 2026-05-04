# ZDI-11-250: Apple QuickTime STTS atom Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-250
- **ZDI-CAN:** ZDI-CAN-1163
- **Date:** 2011-08-09
- **CVE:** CVE-2011-0252
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Matt "j00ru" Jurczyk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-250/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime handles invalid Sample Duration values in the Time-To-Sample atoms. This value is used in the calculation of a loop counter. If this counter is too big it will result in a heap overflow that can cause remote code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4826

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2011-08-09 - Coordinated public release of advisory
