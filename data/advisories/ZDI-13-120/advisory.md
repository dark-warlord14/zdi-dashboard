# ZDI-13-120: ABB DataManager National Instruments Multiple ActiveX Controls cwui.ocx ExportStyle() Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-120
- **ZDI-CAN:** ZDI-CAN-1554
- **Date:** 2013-06-11
- **CVE:** CVE-2013-5021
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** ABB
- **Affected Products:** DataManager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-120/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ABB DataManager Data Analysis. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within multiple 3rd party CWUI activex controls. CWNumEdit, CWGraph, CWBoolean, CWSlide, and CWKnob all support an ExportStyle() method that allows creation of an arbitrary file with the desired extension and inside an arbitrary location. File content can be controlled by setting a 'Caption' or 'FormatString' property. This vulnerability can be leveraged by an attacker to execute code under the context of the current process.

## Additional Details

ABB has issued an update to correct this vulnerability. More details can be found at: http://www05.abb.com/global/scot/scot203.nsf/veritydisplay/5975a8a86c82eec2c125798e00551522/$file/SECURITY_BULLETIN_-_ABBVU-PACT-3BSE072617_DataManager_Vulnerability.pdf

## Disclosure Timeline

- 2012-12-04 - Vulnerability reported to vendor
- 2013-06-11 - Coordinated public release of advisory
