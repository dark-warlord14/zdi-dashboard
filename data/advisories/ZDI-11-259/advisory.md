# ZDI-11-259: Apple QuickTime STSZ atom Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-259
- **ZDI-CAN:** ZDI-CAN-1162
- **Date:** 2011-08-16
- **CVE:** CVE-2011-0251
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Matt "j00ru" Jurczyk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-259/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime handles corrupt Sample Size atoms. When the value for 'Number of Entries' in this atom differs from the 'Number of Entries' in the Time-To-Sample atom, Quicktime will fill the Atom Sample Table with uninitialized data read from memory. This can later on result in a heap overflow when the data is used to calculate a loop counter to fill a heap buffer.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4826

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory
