# ZDI-15-393: Foxit Reader TIFF Conversion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-393
- **ZDI-CAN:** ZDI-CAN-2902
- **Date:** 2015-08-17
- **CVE:** N/A
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Foxit Reader
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-393/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the conversion of TIFF files into PDF format. By providing a malformed TIFF, an attacker can cause Foxit Reader to read a VTable from an invalid location. This could allow an attacker to execute arbitrary code under the context of the Reader process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php#FRD-31

## Disclosure Timeline

- 2015-04-24 - Vulnerability reported to vendor
- 2015-08-17 - Coordinated public release of advisory
