# ZDI-15-043: SolarWinds Server and Application Monitor TSUnicodeGraphEditorControl factory.loadExtensionFactory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-043
- **ZDI-CAN:** ZDI-CAN-2379
- **Date:** 2015-02-10
- **CVE:** CVE-2015-1501
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SolarWinds
- **Affected Products:** Server and Application Monitor
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-043/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Server and Application Monitor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the 'factory' object's loadExtensionFactory method. By supplying a UNC path to a controlled binary, a remote attacker can execute arbitrary code under the context of the process.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: http://downloads.solarwinds.com/solarwinds/Release/HotFix/OrionPlatform-2014.2.1-HotFix7.zip

## Disclosure Timeline

- 2014-09-03 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
