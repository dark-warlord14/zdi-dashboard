# ZDI-10-259: Apple QuickTime FPX Subimage Count Out-of-bounds Counter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-259
- **ZDI-CAN:** ZDI-CAN-681
- **Date:** 2010-12-07
- **CVE:** CVE-2010-3801
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-259/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required in that a user must be coerced into opening up a malicious document or visiting a malicious website. The specific flaw exists within the way the application parses a particular property out of a flashpix file. The application will explicitly trust a field in the property as a length for a loop over an array of data structures. If this field's value is larger than the number of objects, the application will utilize objects outside of this array. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4447

## Disclosure Timeline

- 2010-06-01 - Vulnerability reported to vendor
- 2010-12-07 - Coordinated public release of advisory
