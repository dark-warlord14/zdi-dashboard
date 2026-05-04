# ZDI-15-044: SolarWinds Server and Application Monitor TSUnicodeGraphEditorControl graphManager.load Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-044
- **ZDI-CAN:** ZDI-CAN-2380
- **Date:** 2015-02-10
- **CVE:** CVE-2015-1500
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SolarWinds
- **Affected Products:** Server and Application Monitor
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-044/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Server and Application Monitor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the 'graphManager' object's load method. The issue lies in a failure to validate the size of an attacker-supplied input before copying it into a fixed-size buffer on the stack. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://downloads.solarwinds.com/solarwinds/Release/HotFix/OrionPlatform-2014.2.1-HotFix7.zip

## Disclosure Timeline

- 2014-09-03 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
